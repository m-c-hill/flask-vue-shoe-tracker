<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootstrap CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
      />
      <h1 class="text-center bg-primary text-white" style="border-radius: 12px">
        Shoe Tracker 👟
      </h1>
      <br />
      <btn-toolbar>
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.shoe-modal
        >
          Add Shoe
        </button>
        <button type="button" class="btn btn-warning btn-sm">Log Run</button>
      </btn-toolbar>
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
      <footer
        class="bg-primary text-white text-center"
        style="border-radius: 12px"
      >
        Test
      </footer>

      <!-- Modal -->

      <b-modal
        ref="addShoeModal"
        id="shoe-modal"
        title="Add a New Shoe"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addShoeForm.model"
              required
              placeholder="Enter Shoe"
            ></b-form-input>
          </b-form-group>

          <button type="submit" variant="primary">Submit</button>
          <button type="reset" variant="primary">Reset</button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      shoes: [],
      addShoeForm: {
        model: "",
      },
    };
  },

  methods: {
    // GET Function
    getShoes() {
      const path = "http://localhost:5000/shoes";
      axios
        .get(path)
        .then((res) => {
          this.shoes = res.data.resource.shoes;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // POST Function
    addShoe(payload) {
      const path = "http://localhost:5000/new_shoe";
      axios.post(path, payload).then(() => {
        this.getShoes();
      });
    },

    initForm() {
      this.addShoeForm.model = "";
    },

    onSubmit(event) {
      event.preventDefault();
      this.$refs.addShoeModal.hide();
      const payload = {
        model: this.addShoeForm.title,
      };
      this.addShoe(payload);
      this.initForm;
    },

    onReset(event) {
      event.preventDefault();
      this.$ref.addShoeModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getShoes();
  },
};
</script>
