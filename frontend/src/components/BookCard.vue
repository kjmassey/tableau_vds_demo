<template>
    <div class="px-4 py-4">
        <v-card max-width="400" variant="tonal" elevation="0">
            <v-card-item>
                <v-card-title>
                    <div class="card-subtitle">
                        <div>{{ this.$props.title.length < 25 ? this.$props.title : `${this.$props.title.slice(0,
                            24)}...` }}</div>
                                <div>
                                    <v-chip density="compact" :color="this.genreColors[book['Super Genre']]"
                                        variant="flat">
                                        {{ this.$props.genre }}
                                    </v-chip>
                                </div>
                        </div>
                </v-card-title>
                <v-card-subtitle>
                    <div class="card-subtitle">
                        <div>by {{ this.$props.author }}</div>
                        <div class="text-caption">{{ this.$props.copiesAvailable }} available</div>
                    </div>
                </v-card-subtitle>
                <v-card-subtitle class="text-caption">({{ this.$props.releaseYear }})</v-card-subtitle>

            </v-card-item>
            <v-card-text v-if="this.$props.genreRank <= 3">
                <div class="d-flex text-body-1 justify-center align-center">
                    <div class="px-1"><v-icon icon="mdi-star" size="24" color="yellow"></v-icon></div>
                    <div>#{{ this.$props.book['Genre Rank'] }} in {{ this.$props.genre }}</div>
                </div>
            </v-card-text>
            <v-card-text>
                <div class="cover-image py-2">
                    <div class="pb-2">
                        <v-img :width="225" cover :src="this.$props.imgUrl"></v-img>
                    </div>
                </div>
                <div class="text-body-1">
                    <em>
                        "{{ this.$props.synopsis }}"
                    </em>
                </div>
                <div class="py-4">
                    <div class="pb-4 text-caption">Recent Checkout History:</div>
                    <v-sparkline :labels="sparkLabels" :model-value="this.$props.checkOutHistory" :smooth="16"
                        line-width="2" show-labels></v-sparkline>
                </div>
            </v-card-text>
            <v-card-actions>
                <div class="button-justify-center pb-2">
                    <div class="text-caption pl-2">Checked out <strong>{{ this.$props.totalCheckouts }}x</strong> (last
                        6 mos.)</div>
                    <v-btn prepend-icon="mdi-cart" variant="tonal"
                        @click="$emit('addBook', this.$props.book); inCart = !inCart" v-if="!inCart">Add to
                        Cart</v-btn>
                    <v-btn prepend-icon="mdi-check" variant="flat" color="green" disabled v-else>In Cart</v-btn>
                </div>
            </v-card-actions>

        </v-card>
    </div>
</template>

<script>
export default {
    data: () => ({
        sparkLabels: [
            'Oct 23',
            'Nov 23',
            'Dec 23',
            'Jan 24',
            'Feb 24',
            'Mar 24'
        ],
        inCart: false,
        genreColors: {
            "Fiction": "#ff0000",
            "Fantasy": "#ff5300",
            "Sci-Fi": "#ffa500",
            "Mystery": "#ffd200",
            "Comedy": "#ffff00",
            "Horror": "#80c000",
            "Romance": "#008000",
            "Adventure": "#004080",
            "Thriller": "#0000ff",
            "Non-Fiction": "#2600c1",
            "YA": "#4b0082"

        }
    }),
    props: { title: String, author: String, genre: String, releaseYear: String, imgUrl: String, synopsis: String, checkOutHistory: Array, copiesAvailable: Number, totalCheckouts: Number, book: Object, genreRank: Number }
}
//
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
    justify-content: space-between;
    align-items: center;
}
</style>