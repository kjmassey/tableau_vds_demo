<template>
  <v-container class="fill-height">

    <v-responsive class="align-center fill-height mx-auto" max-width="1750">
      <div class="d-flex justify-center my-4">
        <div class="text-h2 font-weight-bold">VizQL Data Service (VDS) Report Builder</div>
      </div>
      <div style="height: 80px"></div>
      <div class="d-flex justify-space-evenly">
        <v-card width="500">
          <v-card-item>
            <v-card-title>Orders</v-card-title>
            <v-card-subtitle>Details about individual orders</v-card-subtitle>
          </v-card-item>
          <v-card-text class="py-16">
            <div class="d-flex justify-center py-2">
              <v-icon icon="mdi-invoice-list-outline" size="172" color="blue"></v-icon>
            </div>
          </v-card-text>
          <v-card-actions>
            <div class="d-flex justify-end w-100">
              <v-btn variant="tonal" color="blue"
                @click="this.selectedReport = 'orders'; this.showDialog = true">Generate</v-btn>
            </div>
          </v-card-actions>
        </v-card>
        <v-card width="500">
          <v-card-item>
            <v-card-title>Customers</v-card-title>
            <v-card-subtitle>Details about individual customers</v-card-subtitle>
          </v-card-item>
          <v-card-text class="py-16">
            <div class="d-flex justify-center py-2">
              <v-icon icon="mdi-account-details" size="172" color="blue"></v-icon>
            </div>
          </v-card-text>
          <v-card-actions>
            <div class="d-flex justify-space-between align-center w-100">
              <div class="pl-4">
                <v-switch v-model="repeatCustomers" density="compact" center-affix label="Repeat Customers Only"
                  hide-details color="blue"></v-switch>
              </div>
              <div>
                <v-btn variant="tonal" color="blue"
                  @click="this.selectedReport = 'customers'; this.showDialog = true">Generate</v-btn>
              </div>
            </div>
          </v-card-actions>
        </v-card>
        <v-card width="500">
          <v-card-item>
            <v-card-title>Regions</v-card-title>
            <v-card-subtitle>Details about individual regions</v-card-subtitle>
          </v-card-item>
          <v-card-text class="py-16">
            <div class="d-flex justify-center py-2">
              <v-icon icon="mdi-selection-marker" size="172" color="blue"></v-icon>
            </div>
          </v-card-text>
          <v-card-actions>
            <div class="d-flex justify-space-between w-100">
              <div class="d-flex justify-space-evenly w-75">
                <v-checkbox density="compact" color="blue" hide-details label="East" value="East"
                  v-model="selectedRegions"></v-checkbox>
                <v-checkbox density="compact" color="blue" hide-details label="Central" value="Central"
                  v-model="selectedRegions"></v-checkbox>
                <v-checkbox density="compact" color="blue" hide-details label="South" value="South"
                  v-model="selectedRegions"></v-checkbox>
                <v-checkbox density="compact" color="blue" hide-details label="West" value="West"
                  v-model="selectedRegions"></v-checkbox>
              </div>
              <v-btn variant="tonal" color="blue"
                @click="this.selectedReport = 'regions'; this.showDialog = true">Generate</v-btn>
            </div>
          </v-card-actions>
        </v-card>
      </div>
    </v-responsive>

  </v-container>
  <ReportDialog v-if="showDialog" :report-name="selectedReport" @close-dialog="this.showDialog = false"
    :repeat-customers="repeatCustomers" :selected-regions="this.selectedRegions" />
</template>

<script>
export default {
  data: () => ({
    showDialog: false,
    selectedReport: '',
    repeatCustomers: false,
    selectedRegions: ["East", "Central", "South", "West"]
  })
}
</script>
