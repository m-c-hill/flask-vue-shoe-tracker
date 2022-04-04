<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootstrap CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
      />
      <h1>Shoe Tracker</h1>
      <br />
      <button type="button" class="btn btn-success">Add Shoe</button>
      <br />
      <br />
      <div class="row">
        <div class="col-sm-12"></div>
        <!-- Alert message -->
        <table class="table">
          <thead>
            <tr>
              <!-- Table header cells -->
              <th scope="col">Brand</th>
              <th scope="col">Model</th>
              <th scope="col">Nickname</th>
              <th scope="col">Distance (km)</th>
              <th scope="col">Notes</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(shoe, index) in shoes" :key="index">
              <!-- Dummy data to be removed -->
              <td>{{ shoe.brand_id }}</td>
              <td>{{ shoe.model }}</td>
              <td>{{ shoe.nickname }}</td>
              <td>{{ shoe.distance }}</td>
              <td>{{ shoe.notes }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-info btn-sm">
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      shoes: [],
    };
  },

  methods: {
    getShoes() {
      const path = "http://localhost:5000/shoes";
      axios
        .get(path)
        .then((res) => {
          this.shoes = res.data.shoes;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getShoes();
  },
};
</script>
