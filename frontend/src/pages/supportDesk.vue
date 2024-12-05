<template>
    <v-overlay :model-value="showLoader" class="align-center justify-center">
        <v-progress-circular indeterminate></v-progress-circular>
    </v-overlay>
    <v-container class="fill-height">
        <v-app-bar elevation="2" scroll-behavior="elevate">
            <template v-slot:prepend>
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            </template>
            <v-app-bar-title>DataFam Support Desk</v-app-bar-title>
            <div class="text-h6">
                {{ currentSection }}
            </div>
            <v-spacer></v-spacer>
            <v-btn rounded :ripple="false">
                <v-badge :color="notificationCount < 1 ? 'transparent' : 'blue'"
                    :content="notificationCount > 0 ? notificationCount : ''">
                    <v-menu activator="parent">
                        <v-list>
                            <v-list-subheader>
                                You have {{ notificationCount }} notifications
                            </v-list-subheader>
                            <v-list-item v-if="pastDueCount > 0" class="my-4">
                                <v-list-item-title>Past Due Items</v-list-item-title>
                                <v-list-item-subtitle>You have {{ pastDueCount }} past due
                                    item(s)!</v-list-item-subtitle>
                            </v-list-item>
                            <v-list-item v-if="escalatedCount > 0" class="my-4"><v-list-item-title>Escalated
                                    Items</v-list-item-title>
                                <v-list-item-subtitle>You have {{ escalatedCount }} escalated
                                    item(s)!</v-list-item-subtitle></v-list-item>
                        </v-list>
                    </v-menu>
                    <v-icon icon="mdi-bell-outline" size="28"></v-icon>
                </v-badge>
            </v-btn>
            <div class="px-4">
                <v-avatar image="../assets/ambassadorheadshot.png" size="36"></v-avatar>
            </div>
        </v-app-bar>

        <v-responsive class="fill-height mx-auto justify-center w-100"
            :class="currentSection == 'My Team' || currentSection == 'Analytics' ? 'align-start' : 'align-center'">
            <div class="w-100 fill-height">
                <template v-if="currentSection == 'My Tickets' && !showLoader">
                    <div class="d-flex justify-center pb-4">
                        <v-tabs v-model="currentTab">
                            <v-tab v-for="item in [
                                'All Open',
                                'Past Due',
                                'Escalated',
                                'All Closed',
                            ]" :text="item" :value="item"></v-tab>
                        </v-tabs>
                    </div>
                    <ServiceDeskTicket v-for="ticket in tickets && selectedTickets" :ticketItem="ticket" />
                </template>
                <ServiceDeskTeam :tickets="tickets && tickets" v-if="currentSection == 'My Team'" />
                <div v-if="currentSection == 'Analytics'" style="align-self: start">
                    <ServiceDeskAnalytics />
                </div>
            </div>
        </v-responsive>
        <v-navigation-drawer v-model="drawer" :location="$vuetify.display.mobile ? 'bottom' : undefined" temporary
            width="350">
            <v-list lines="two">
                <v-list-item title="Welcome, Kyle!" :subtitle="`Happy ${currentDayName}`"></v-list-item>
                <v-divider></v-divider>
                <v-list-item link title="My Tickets" @click="currentSection = 'My Tickets'">
                    <template v-slot:prepend>
                        <v-icon icon="mdi-ticket-outline" size="32"></v-icon>
                    </template>
                    <template v-slot:append>
                        <v-badge inline color="yellow" :content="waitingForUserCount"> </v-badge>
                        <v-badge inline color="red" :content="waitingForMeCount"> </v-badge>
                    </template>
                </v-list-item>
                <v-list-item link title="My Team" @click="currentSection = 'My Team'">
                    <template v-slot:prepend>
                        <v-icon icon="mdi-account-multiple-outline" size="32"></v-icon>
                    </template>
                </v-list-item>

                <v-list-item link title="Analytics" @click="currentSection = 'Analytics'">
                    <template v-slot:prepend>
                        <v-icon icon="mdi-chart-bar"></v-icon>
                    </template>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </v-container>
</template>

<script>
import ServiceDeskTicket from "@/components/ServiceDeskTicket.vue";
import ServiceDeskTeam from "@/components/ServiceDeskTeam.vue";
import ServiceDeskAnalytics from "@/components/ServiceDeskAnalytics.vue"
import axios from "axios";

export default {
    data: () => ({
        showLoader: true,
        drawer: false,
        currentSection: "My Tickets",
        currentTab: "All Open",
        items: [],
        tickets: [],
        currentUser: "Kyle Massey"
    }),

    components: { ServiceDeskTicket, ServiceDeskTeam, ServiceDeskAnalytics },
    computed: {
        currentDayName() {
            // create a new Date object
            const now = new Date();

            // get the current day of the week
            const daysOfWeek = [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
            ];

            return daysOfWeek[now.getDay()];
        },
        selectedTickets() {
            switch (this.currentTab) {
                case "All Open":
                    return (
                        this.tickets &&
                        this.tickets.filter(
                            (e) => e.assignee == this.currentUser && e.status != "Closed"
                        )
                    );

                case "Past Due":
                    return (
                        this.tickets &&
                        this.tickets.filter(
                            (e) =>
                                e.assignee == this.currentUser &&
                                e.isPastDue &&
                                e.status != "Closed"
                        )
                    );

                case "Escalated":
                    return (
                        this.tickets &&
                        this.tickets.filter(
                            (e) =>
                                e.assignee == this.currentUser &&
                                e.escalated &&
                                e.status != "Closed"
                        )
                    );

                case "All Closed":
                    return (
                        this.tickets &&
                        this.tickets.filter(
                            (e) => e.assignee == this.currentUser && e.status == "Closed"
                        )
                    );
            }
        },
        notificationCount() {
            let notificationCount = 0;

            this.tickets &&
                this.tickets.filter(
                    (e) =>
                        e.isPastDue && e.status != "Closed" && e.assignee == this.currentUser
                ).length > 0
                ? (notificationCount += 1)
                : (notificationCount += 0);
            this.tickets &&
                this.tickets.filter(
                    (e) =>
                        e.escalated &&
                        e.status != "Closed" &&
                        e.assignee == this.currentUser
                ).length > 0
                ? (notificationCount += 1)
                : (notificationCount += 0);

            return notificationCount;
        },
        pastDueCount() {
            return (
                this.tickets &&
                this.tickets.filter(
                    (e) =>
                        e.isPastDue &&
                        e.status != "Closed" &&
                        e.assignee == this.currentUser
                ).length
            );
        },
        escalatedCount() {
            return (
                this.tickets &&
                this.tickets.filter(
                    (e) =>
                        e.escalated &&
                        e.status != "Closed" &&
                        e.assignee == this.currentUser
                ).length
            );
        },
        waitingForMeCount() {
            return this.tickets && this.tickets.filter(e => e.status == 'Waiting for Support' && e.status != 'Closed' && e.assignee == this.currentUser).length
        },
        waitingForUserCount() {
            return this.tickets && this.tickets.filter(e => e.status == 'Waiting for User' && e.status != 'Closed' && e.assignee == this.currentUser).length
        }
    },
    methods: {
        async getData() {
            await axios
                .get("http://localhost:8000/supportDesk")
                .then((response) => {
                    this.tickets = response.data;
                    this.showLoader = false;
                })
                .catch((error) => {
                    console.log("ERROR: ", error);
                    this.showLoader = False;
                });
        },
        formattedTicketAge(openDateStr) {
            const timeAgo = new TimeAgo("en-US");
            return timeAgo.format(new Date(openDateStr));
        },
    },
    async mounted() {
        await this.getData();
    },
};
</script>

<style scoped>
.notification-icon {
    cursor: pointer;
}
</style>
