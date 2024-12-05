<template>
    <v-container class="fill-height">
        <v-responsive class="align-centerfill-height mx-auto" max-width="900">
            <div>
                <!-- <v-chip-group v-model="selectedPills" multiple>
                    <v-chip v-for="pill in availablePills" color="primary" variant="tonal" selectable>
                        {{ pill.name }}
                    </v-chip>
                </v-chip-group> -->
                <v-btn @click="runBasicQuery()">Clicky</v-btn>
            </div>
            <div class="py-4">
                <v-data-table :items="this.basicQueryData && this.basicQueryData" :loading="isLoading"></v-data-table>
            </div>
            <div class="py-4">
                <download-csv class="btn btn-default" :data="this.basicQueryData" name="filename.csv">

                    <v-btn>Download CSV (This is a slot)</v-btn>

                </download-csv>
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
        availablePills: [
            {
                'name': 'Category'
            },
            {
                'name': 'Sub-Category'
            },
            {
                'name': 'State'
            }
        ],
        selectedPills: [],
        basicQueryData: []
    }),
    components: {
        downloadCsv
    },
    computed: {
        basicComputedHeaders() {
            try {
                return Object.keys(this.basicQueryData.data[0])
            } catch (e) {
                return null

            }
        },
        queryData() {
            if (this.basicQueryData && this.basicQueryData.length > 0) {
                var newList = []

                this.basicQueryData.forEach(e => {


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

            await axios.get('http://localhost:8000/basicQuery').then(response => {
                var formattedResp = []
                console.log('FORMATTED RESP: ', formattedResp)

                console.log('+++++ ', response.data.data)

                response.data.data.forEach(e => {
                    // Add prev month
                    var prevDate = new Date(e['Order Month-Year'])
                    prevDate.setMonth(prevDate.getMonth() - 1)

                    e.prevMonth = prevDate.toLocaleDateString()

                    // Format order date
                    var oDate = new Date(e['Order Month-Year'])
                    e['Order Month-Year'] = oDate.toLocaleDateString()

                    // Prev Month Sales
                    e['Prev Month Sales'] = response.data.data.find(x => x['Order Month-Year'].toLocaleDateString() == e.prevMonth && x['Category'] == e['Category'] && x['Sub-Category'] == e['Sub-Category'])

                    formattedResp.push(e)
                })

                console.log('FORMATTED RESP: ', formattedResp)
                this.basicQueryData = formattedResp
                this.isLoading = false
            }).catch(err => {
                console.log('ERROR: ', err)
                this.isLoading = false
            })
        }
    }
}
</script>