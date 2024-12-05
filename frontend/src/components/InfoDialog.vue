<template>
    <v-dialog :model-value="this.$props.show" persistent max-width="800">
        <v-card variant="flat" v-if="!showConfirmation">
            <v-card-item>
                <v-card-title>VizQL Data Service: Your Data, Your Way</v-card-title>
                <v-card-subtitle>It's never been easier to use <em>your</em> data to do what <em>you</em>
                    want!</v-card-subtitle>
            </v-card-item>
            <v-card-text>
                <div>
                    <p>See my related blog post for the full background of what you see here:</p>
                    <p>[[LINK TO ARTICLE]]</p>
                </div>
                <div class="d-flex no-wrap justify-space-between w-100 pt-4">
                    <div class="d-flex">
                        <v-icon icon="mdi-link"></v-icon>
                        <div class="pl-1"><a href='https://kylejmassey.com' target='_blank'>kylejmassey.com</a></div>
                    </div>
                    <div class="d-flex">
                        <v-icon icon="mdi-twitter"></v-icon>
                        <div class="pl-1"><a href='https://twitter.com/UpInYourVizness'
                                target='_blank'>@UpInYourVizness</a></div>
                    </div>
                    <div class="d-flex">
                        <v-icon icon="mdi-linkedin"></v-icon>
                        <div class="pl-1"><a href='https://www.linkedin.com/in/kylejmassey/' target='_blank'>Kyle J.
                                Massey</a></div>
                    </div>
                    <div class="d-flex">
                        <v-icon icon="mdi-github"></v-icon>
                        <div class="pl-1"><a href='http://github.com/kjmassey?tab=repositories'
                                target='_blank'>kjmassey</a>
                        </div>
                    </div>
                </div>
            </v-card-text>
            <v-card-actions>
                <v-btn variant="compact" @click="$emit('closeInfoDialog')">Close</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</template>

<script>
export default {
    data: () => ({

    }),
    props: { show: Boolean }
}
</script>

<style scoped></style>