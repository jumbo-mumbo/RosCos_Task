<template>
    <div class="albums_container">
        <div class="albums_content">
            <h1>Albums</h1>
            <table class="albums_table">
                <tr>
                    <th>album</th>
                    <th align="center">
                        name
                        <tr>
                            <button @click="sortByName">sort</button>
                        </tr>
                    </th>
                    <th align="center">
                        artist@name
                        <tr>
                            <button @click="sortByArtist()">sort</button>
                        </tr>
                    </th>
                    <th>tracks</th>
                </tr>
                <tr v-for="album in albums" :key="album.id">
                    <td>{{album.album}}</td>
                    <td>{{album.name}}</td>
                    <td>{{album['artist@name']}}</td>
                    <td align="center">
                        <tr v-for="track in album.tracks">
                            {{track}}
                        </tr>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // albums
                albums: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.$http.get(
                        'http://localhost:8000/api/albums/'
                        );
                    // set the data returned as tasks
                    this.albums = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },

            async sortByArtist(){
                try {
                    const response = await this.$http.get(
                        'http://localhost:8000/api/albums/?ordering=artist'
                        );
                    this.albums = response.data;

                } catch (error) {
                    console.log(error)
                }
            },

            async sortByName(){
                try {
                    const response = await this.$http.get(
                        'http://localhost:8000/api/albums/?ordering=name'
                        );
                    this.albums = response.data;

                } catch (error) {
                    console.log(error)
                }
            },

            
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>

<style>
table, th, td {
  border:1px solid black;
}
</style>