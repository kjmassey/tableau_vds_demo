<template>

    <v-dialog :model-value="this.$props.show && this.$props.selectedBooks.length > 0" persistent max-width="800">
        <v-card variant="flat" v-if="!showConfirmation">
            <v-card-item>
                <v-card-title>Ready to Check Out?</v-card-title>
                <v-card-subtitle>Review your selections</v-card-subtitle>
            </v-card-item>
            <v-card-text>
                <div v-for="book in this.$props.selectedBooks" class="d-flex align-center py-4">
                    <div class="px-2">
                        <v-img width="64" cover :src="book['Cover URL']"></v-img>
                    </div>
                    <div class="px-2 d-flex space-between w-100 align-center">
                        <div class="w-100">
                            <div class="text-h5">{{ book['Book Title'] }}</div>
                            <div class="text-subtitle">{{ book['Author'] }}</div>
                        </div>
                        <div><v-btn variant="flat" @click="$emit('bookRemoved', book)"><v-icon icon="mdi-delete-outline"
                                    size="28" color="red"></v-icon></v-btn></div>
                    </div>
                </div>
            </v-card-text>
            <v-card-actions>
                <v-btn @click="$emit('closeCheckoutDialog')" density="compact" variant="flat">Close</v-btn>
                <v-btn color="primary" @click="this.showConfirmation = true">Reserve {{ this.$props.selectedBooks.length
                    }} Book{{
                        this.$props.selectedBooks.length > 1 ? 's' : '' }}</v-btn>
            </v-card-actions>
        </v-card>
        <v-card variant="flat" v-else>
            <v-card-item>
                <v-card-title>You're all set!</v-card-title>
                <v-card-subtitle>See a librarian to pick up your reservations</v-card-subtitle>
            </v-card-item>
            <v-card-text>
                <div class="d-flex justify-center py-4">
                    <v-icon icon="mdi-check-outline" color="green" size="112"></v-icon>
                </div>
            </v-card-text>
            <v-card-actions>
                <v-btn @click="$emit('closeCheckoutDialog')" density="compact" variant="flat">Close</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    data: () => ({
        showConfirmation: false
    }),
    props: { show: Boolean, selectedBooks: Array },
    methods: {


    }
}

</script>

<style scoped></style>
