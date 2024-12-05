<template>
    <div class="d-flex justify-center">
        <v-card max-width="1100" class="flex-grow-1 my-4 py-2" rounded elevated elevation="5">
            <v-card-item>
                <v-card-title class="mb-0 pb-0">
                    <div class="d-flex justify-space-between">
                        <div class="text-h5">
                            #{{ $props.ticketItem.number }} - {{ $props.ticketItem.shortDescription }}
                        </div>
                        <div>
                            <v-chip :color="this.statusColor($props.ticketItem.status)" elevated class="mx-2">{{
                                $props.ticketItem.status }}</v-chip>

                            <v-tooltip location="top" :text="`Reported by ${$props.ticketItem.reporter}`">
                                <template v-slot:activator="{ props }">
                                    <v-avatar color="blue" v-bind="props" size="32" class="mx-2">
                                        <div>{{ $props.ticketItem.reporter.substring(0, 1) }}</div>
                                    </v-avatar>
                                </template>
                            </v-tooltip>
                            <template v-if="$props.ticketItem.escalated">
                                <v-tooltip text="Escalated" location="top">
                                    <template v-slot:activator="{ props }">
                                        <v-icon icon="mdi-exclamation" color="orange" v-bind="props"></v-icon>
                                    </template>
                                </v-tooltip>
                            </template>
                            <template v-if="$props.ticketItem.isPastDue">
                                <v-tooltip text="Past Due" location="top">
                                    <template v-slot:activator="{ props }">
                                        <v-icon icon="mdi-fire-alert" color="red" v-bind="props"></v-icon>
                                    </template>
                                </v-tooltip>
                            </template>
                        </div>
                    </div>
                    <div class="text-caption my-0 py-0">Opened {{ this.formattedTicketAge($props.ticketItem.opened) }}
                    </div>
                </v-card-title>
            </v-card-item>
            <v-card-text class="pt-4">
                <div
                    style="-webkit-line-clamp: 8; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden;">
                    {{ $props.ticketItem.details }}
                </div>
            </v-card-text>
            <v-card-actions class="d-flex justify-space-between">
                <div class="px-2 font-italic">
                    {{ $props.ticketItem.comments.length }} comment{{ comments.length == 1 ? '' : 's' }}
                </div>
                <v-btn elevated variant="outlined" color="primary" class="text-none" @click="dialog = true">View
                    Details</v-btn>
            </v-card-actions>
        </v-card>
        <v-dialog v-model="dialog" max-width="800" persistent>
            <v-card transition="v-slide-y-reverse-transition">
                <v-card-title>
                    <div class="d-flex justify-space-between align-center">
                        <div>
                            Details for #{{ $props.ticketItem.number }}
                        </div>
                        <div>
                            <v-btn icon="mdi-close" density="compact" @click="dialog = false"> </v-btn>
                        </div>
                    </div>
                </v-card-title>
                <v-card-text>
                    <div class="d-flex justify-space-between align-center text-caption">
                        <div>Reporter: {{ $props.ticketItem.reporter }}</div>
                        <div>Opened {{ formattedTicketAge($props.ticketItem.opened) }}</div>
                    </div>
                </v-card-text>
                <v-card-text>
                    {{ $props.ticketItem.details }}

                </v-card-text>
                <v-card-text>
                    <v-expansion-panels elevation="0">
                        <v-expansion-panel density="compact" color="primary">
                            <v-expansion-panel-title>Comments</v-expansion-panel-title>
                            <v-expansion-panel-text>
                                {{ $props.ticketItem.comments }}</v-expansion-panel-text>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </v-card-text>
                <v-card-text>
                    <v-textarea placeholder="Add a comment / respond to user" no-resize variant="outlined"></v-textarea>
                </v-card-text>
                <v-card-actions>
                    <div class="d-flex justify-space-between align-center w-100 px-2 pb-2">
                        <div>
                            <v-btn color="green" variant="outlined">Close Ticket</v-btn>
                        </div>
                        <div>
                            <v-btn variant="outlined">Send to User</v-btn>
                        </div>
                    </div>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import TimeAgo from 'javascript-time-ago';
import en from 'javascript-time-ago/locale/en'

export default {
    data: () => ({
        drawer: false,
        items: [],
        notifications: 5,
        dialog: false,
        comments: ['Comment1', 'Comment2']
    }),
    props: { ticketItem: Object },
    computed: {
        currentDayName() {
            // create a new Date object
            const now = new Date();

            // get the current day of the week
            const daysOfWeek = [
                'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
            ];

            return daysOfWeek[now.getDay()]
        }

    },
    methods: {
        statusColor(status) {
            switch (status) {
                case 'Waiting for Support':
                    return 'red'

                case 'Waiting for User':
                    return 'yellow'

                default:
                    return 'green'
            }
        },
        formattedTicketAge(dateStr) {
            const timeAgo = new TimeAgo('en-US')
            return timeAgo.format(new Date(dateStr))
        },

    }
};

TimeAgo.addDefaultLocale(en)
</script>

<style scoped></style>