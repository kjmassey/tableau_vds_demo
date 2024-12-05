<template>
    <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />

</template>
<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, BarElement, CategoryScale, LinearScale)

export default {
    data: () => ({
        chartOptions: { responsive: true, legend: false }
    }),
    props: { dataPoints: Array },
    components: { Bar },
    props: {
        chartData: {
            type: Object,
            required: true
        },
        chartOptions: {
            type: Object,
            default: () => { }
        }
    }
}

</script>
<style scoped></style>