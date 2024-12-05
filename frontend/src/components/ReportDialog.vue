<template>

    <v-dialog :model-value="true" persistent max-width="1100">
        <v-card variant="flat">
            <v-card-item>
                <v-card-title v-if="isLoading">Your Report is Being Generated</v-card-title>
                <v-card-title v-else>Your Report is Ready</v-card-title>
                <v-card-subtitle v-if="!isLoading">Preview below and then download to explore!</v-card-subtitle>
            </v-card-item>
            <v-card-text>
                <div class="d-flex justify-center align-center w-100" v-if="isLoading">
                    <v-progress-circular indeterminate></v-progress-circular>
                </div>
                <OrdersTable v-if="this.$props.reportName == 'orders'" @report-loading="isLoading = true"
                    @report-ready="isLoading = false" @emit-report-data="setData" />

                <CustomersTable v-if="this.$props.reportName == 'customers'" @report-loading="isLoading = true"
                    @report-ready="isLoading = false" :repeat-customers="this.$props.repeatCustomers"
                    @emit-report-data="setData" />
                <RegionsTable v-if="this.$props.reportName == 'regions'" @report-loading="isLoading = true"
                    @report-ready="isLoading = false" :selected-regions="this.$props.selectedRegions"
                    @emit-report-data="setData" />

            </v-card-text>
            <v-card-actions>
                <v-btn @click="$emit('closeDialog')" variant="flat">Close</v-btn>
                <download-csv class="btn btn-default" :data="this.reportData" name="filename.csv">
                    <v-btn color="primary">Download</v-btn>
                </download-csv>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import OrdersTable from './OrdersTable.vue';
import CustomersTable from './CustomersTable.vue';
import RegionsTable from './RegionsTable.vue';
import downloadCsv from 'vue-json-csv'


export default {
    data: () => ({
        showConfirmation: false,
        isLoading: true,
        reportData: []
    }),
    props: { reportName: String, repeatCustomers: Boolean, selectedRegions: Array },
    components: { OrdersTable, CustomersTable, RegionsTable, downloadCsv },
    methods: {
        setData(e) {
            this.reportData = e
        }

    }
}

</script>

<style scoped></style>
