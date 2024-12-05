<template>
    <div class="fab" v-if="this.selectedBooks.length > 0">
        <v-fab prepend-icon="mdi-cart" color="success" size="50" extended @click="this.showCheckoutDialog = true">
            <div>{{ this.selectedBooks.length }}</div>
        </v-fab>
    </div>
    <v-container class="fill-height">
        <v-overlay :model-value="showLoader" class="align-center justify-center">
            <v-progress-circular indeterminate></v-progress-circular>
        </v-overlay>
        <v-app-bar app fixed color="#004080
">
            <div class="navbar px-4"><v-icon icon="mdi-library" size="36"></v-icon>
                <div class="text-h5 pl-4">#DataFam
                    Library</div>
            </div>
            <v-spacer></v-spacer>
            <div class="pr-4">
                <v-btn @click="showInfoDialog = true">
                    <v-icon icon="mdi-information-outline" size="32" /></v-btn>
            </div>
        </v-app-bar>
        <v-responsive class="align-center fill-height mx-auto">
            <div class="py-2 d-flex justify-center" v-if="!this.showLoader">
                <v-select label="Sort By:"
                    :items="['Title', 'Author', 'Genre', 'Release Year', 'Total Checkouts (6 mos.)']" variant="outlined"
                    density="compact" max-width="325" v-model="selectedSort"
                    @update:modelValue="changeBookSort(selectedSort)"></v-select>
            </div>
            <div class="book-grid">
                <book-card v-for="book in bookData" :key="book['Book Id']" :title="book['Book Title']"
                    :genre="book['Super Genre']" :author="book.Author" :releaseYear="book['Release Year']"
                    :imgUrl="book['Cover URL']" :synopsis="book.Synopsis" :checkOutHistory="book['checkout history']"
                    :copiesAvailable="book['Available Copies']" :totalCheckouts="book['Total Checkouts']" :book="book"
                    :genreRank="book['Genre Rank']" @add-book="addBookToCart" />
            </div>
        </v-responsive>
        <checkout-dialog :show="showCheckoutDialog" :selected-books="this.selectedBooks"
            @close-checkout-dialog="this.showCheckoutDialog = false; reloadPage()" @book-removed="removeBookFromCart" />
        <info-dialog :show="showInfoDialog" @close-info-dialog="this.showInfoDialog = false" />

    </v-container>


</template>

<script>
import BookCard from '@/components/BookCard.vue';
import CheckoutDialog from '@/components/CheckoutDialog.vue'
import InfoDialog from '@/components/InfoDialog.vue';
import axios from 'axios'

export default {
    data: () => ({
        bookData: {},
        showLoader: true,
        selectedSort: null,
        selectedBooks: [],
        showCheckoutDialog: false,
        showInfoDialog: false
    }),
    components: { BookCard, CheckoutDialog, InfoDialog },
    methods: {
        async getLibraryData() {
            await axios.get('http://localhost:8000/libraryQuery').then(response => {
                this.bookData = response.data.data
            }).catch(e => {
                console.log('ERRROR: ', e)
            })

        },
        changeBookSort(sort) {
            var bookData = JSON.parse(JSON.stringify(this.bookData))

            switch (sort) {
                case 'Author':
                    this.bookData = bookData.sort((a, b) => (a.Author > b.Author) ? 1 : -1)

                    break;

                case 'Title':
                    this.bookData = bookData.sort((a, b) => (a['Book Title'] > b['Book Title']) ? 1 : -1)

                    break;

                case 'Genre':
                    this.bookData = bookData.sort((a, b) => (a['Super Genre'] > b['Super Genre']) ? 1 : -1)

                    break;

                case 'Release Year':
                    this.bookData = bookData.sort((a, b) => (a['Release Year'] > b['Release Year']) ? 1 : -1)

                    break;

                case 'Total Checkouts (6 mos.)':
                    this.bookData = bookData.sort((a, b) => (a['Total Checkouts'] < b['Total Checkouts']) ? 1 : -1)

                    break;

            }
        },
        addBookToCart(e) {
            this.selectedBooks.push(e)
        },
        removeBookFromCart(removedBook) {
            var books = JSON.parse(JSON.stringify(this.selectedBooks))

            this.selectedBooks = books.filter(e => e['Book Id'] !== removedBook['Book Id'])
        },
        reloadPage() {
            this.$router.go()
        }
    },
    async mounted() {
        await this.getLibraryData()
        this.showLoader = false
    }
}

</script>

<style scoped>
.card-subtitle {
    display: flex;
    justify-content: space-between
}

.cover-image {
    display: flex;
    justify-content: center;
}

.button-justify-center {
    width: 100%;
    display: flex;
    justify-content: center;
}

.book-grid {
    justify-content: center;
    display: flex;
    flex-wrap: wrap;

}

.navbar {
    display: flex;
    align-items: center;
}

.fab {
    position: sticky;
    float: right;
    right: 4em;
    top: 2em;
    z-index: 50 !important;
}
</style>
