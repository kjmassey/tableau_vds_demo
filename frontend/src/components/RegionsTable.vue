<template>
    <v-container class="fill-height">
        <v-responsive class="align-centerfill-height mx-auto" v-if="!isLoading">
            <div class="py-4">
                <v-data-table :items="this.queryData && this.queryData" :loading="isLoading"
                    hide-default-footer></v-data-table>
            </div>
            <div v-if="!isLoading">
                Records in Report: {{ this.queryData.length }}

            </div>
        </v-responsive>
    </v-container>
</template>

<script>
import axios from 'axios'
import downloadCsv from 'vue-json-csv'

export default {
    data: () => ({
        isLoading: false,
        queryData: []
    }),
    components: {
        downloadCsv
    },
    props: { selectedRegions: Array },
    computed: {
        basicComputedHeaders() {
            try {
                return Object.keys(this.queryData.data[0])
            } catch (e) {
                return null

            }
        },
        queryData() {
            if (this.queryData && this.queryData.length > 0) {
                var newList = []

                this.queryData.forEach(e => {


                    newList.push(e)
                })

                return newList
            } else {
                return []
            }
        }
    },
    methods: {
        async runBasicQuery() {
            this.isLoading = true

            await axios.post('http://localhost:8000/regions', { "regions": this.$props.selectedRegions }).then(response => {
                this.queryData = response.data.data
                this.$emit('emitReportData', this.queryData)
                this.isLoading = false
            }).catch(err => {
                console.log('ERROR: ', err)
                this.isLoading = false
            })
        }
    },
    async mounted() {
        this.$emit('reportLoading')
        await this.runBasicQuery()
        this.$emit('reportReady')
    }
}
</script>