<template>
    <div class="d-flex justify-center w-100 mt-12">
        <v-card class="mx-4" v-for="member in teamMembers" width="500">
            <v-card-title>
                <div class="d-flex justify-center pt-4">
                    <v-avatar image="../assets/ambassadorheadshot.png" size="96"
                        v-if="member.name == 'Kyle Massey'"></v-avatar>
                    <v-avatar image="../assets/joe.jpg" size="96" v-else-if="member.name == 'Joe Chirilov'"></v-avatar>
                    <v-avatar image="../assets/zak.jpg" size="96" v-if="member.name == 'Zak Geis'"></v-avatar>
                </div>
            </v-card-title>
            <v-card-title>
                <div class="d-flex justify-center">{{ member.name }}</div>
            </v-card-title>
            <v-card-subtitle>
                <div class="d-flex justify-center">{{ member.title }}</div>
            </v-card-subtitle>
            <v-card-text class="mt-4">

                <BarChart id="my-chart-id" :chartData="{
                    labels: ['Open', 'Past Due', 'Escalated', 'Closed'],
                    datasets: [{ data: dataByMember(member.name), backgroundColor: ['red', 'blue', 'green', 'purple'] }]
                }" />
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
// import { Bar } from 'vue-chartjs'
// import { Chart as ChartJS, Title, Tooltip, BarElement, CategoryScale, LinearScale } from 'chart.js'

import BarChart from './BarChart.vue';

export default {
    data: () => ({

    }),
    props: { tickets: Array },
    components: { BarChart },
    methods: {
        dataByMember(memberName) {
            let openCount = this.$props.tickets.filter(e => e.status != 'Closed' && e.assignee == memberName).length
            let pastDueCount = this.$props.tickets.filter(e => e.status != 'Closed' && e.assignee == memberName && e.isPastDue).length
            let escalatedCount = this.$props.tickets.filter(e => e.status != 'Closed' && e.assignee == memberName && e.escalated).length
            let closedCount = this.$props.tickets.filter(e => e.status == 'Closed' && e.assignee == memberName).length

            return [openCount, pastDueCount, escalatedCount, closedCount]
        }
    },
    computed: {
        teamMembers() {
            let members = [
                {
                    name: 'Kyle Massey',
                    title: 'VP Lead Software Enginneer'
                },
                {
                    name: 'Joe Chirilov',
                    title: 'Director, Product Management'
                },
                {
                    name: 'Zak Geis',
                    title: 'Global BI Technology Leader'
                }

            ]

            return members
        }
    }
}

</script>

<style scoped></style>