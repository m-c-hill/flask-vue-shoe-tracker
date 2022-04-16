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

      <b-alert show variant="success" v-if="showMessage">TEST</b-alert>

      <b-btn-toolbar>
        <b-button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.shoe-modal
        >
          Add Shoe
        </b-button>
        <b-button type="button" class="btn btn-warning btn-sm"
          >Log Run</b-button
        >
      </b-btn-toolbar>
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
              <td>{{ shoe.brand.name }}</td>
              <td>{{ shoe.model }}</td>
              <td>{{ shoe.nickname }}</td>
              <td>{{ shoe.distance }}</td>
              <td>{{ shoe.notes }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-info btn-sm"
                    v-b-modal.shoe-update-modal
                    @click="editShoe(shoe)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="deleteShoe(shoe)"
                  >
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

      <!-- New Shoe Modal -->
      <b-modal
        ref="addShoeModal"
        id="shoe-modal"
        title="Add a New Shoe"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group" label="Shoe Details">
            <b-form-select
              id="form-brand-select"
              type="text"
              v-model="addShoeForm.brand"
              :options="brands"
              value-field="id"
              text-field="name"
              placeholder="Brand"
            >
              <!-- <select v-model="brandSelect" class="form-control">
                <option v-for="brand in brands" :key="brand.id" :value="name">
                  {{ brand.name }}
                </option>
              </select> -->
            </b-form-select>
            <b-form-input
              id="form-model-input"
              type="text"
              v-model="addShoeForm.model"
              required
              placeholder="Model"
            ></b-form-input>
            <b-form-input
              id="form-nickname-input"
              type="text"
              v-model="addShoeForm.nickname"
              required
              placeholder="Nickname"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="form-distance-group" label="Distance (km)">
            <b-form-input
              id="form-distance-input"
              type="number"
              v-model="addShoeForm.distance"
              placeholder="Distance (km)"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="form-alert-distance-group"
            label="Alert Distance (km)"
          >
            <b-form-input
              id="form-alert-distance-input"
              type="number"
              v-model="addShoeForm.alertDistance"
              placeholder="Alert Distance (km)"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="form-notes-group"
            label="Shoe Details"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addShoeForm.notes"
              placeholder="Notes"
            ></b-form-input>
          </b-form-group>

          <!-- Buttons to submit and reset -->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>

      <!-- Update Shoe Modal -->
      <b-modal
        ref="editShoeModal"
        id="shoe-update-modal"
        title="Update Shoe"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group id="form-title-group" label="Shoe Details">
            <b-form-select
              id="form-brand-select"
              type="text"
              v-model="editShoeForm.brand"
              :options="brands"
              value-field="id"
              text-field="name"
              placeholder="Brand"
            >
              <!-- <select v-model="brandSelect" class="form-control">
                <option v-for="brand in brands" :key="brand.id" :value="name">
                  {{ brand.name }}
                </option>
              </select> -->
            </b-form-select>
            <b-form-input
              id="form-model-input"
              type="text"
              v-model="editShoeForm.model"
              required
              placeholder="Model"
            ></b-form-input>
            <b-form-input
              id="form-nickname-input"
              type="text"
              v-model="editShoeForm.nickname"
              required
              placeholder="Nickname"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="form-distance-group" label="Distance (km)">
            <b-form-input
              id="form-distance-input"
              type="number"
              v-model="editShoeForm.distance"
              placeholder="Distance (km)"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="form-alert-distance-group"
            label="Alert Distance (km)"
          >
            <b-form-input
              id="form-alert-distance-input"
              type="number"
              v-model="editShoeForm.alertDistance"
              placeholder="Alert Distance (km)"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="form-notes-group"
            label="Shoe Details"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="editShoeForm.notes"
              placeholder="Notes"
            ></b-form-input>
          </b-form-group>
          <!-- Buttons to update and cancel -->
          <b-button-group>
            <b-button type="submit" variant="outline-info">Update</b-button>
            <b-button type="reset" variant="outline-danger">Cancel</b-button>
          </b-button-group>
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
      brands: [],
      shoes: [],
      addShoeForm: {
        brand: "",
        model: "",
        nickname: "",
        distance: "",
        alertDistance: "",
        notes: "",
      },
      editShoeForm: {
        brand: "",
        model: "",
        nickname: "",
        distance: "",
        alertDistance: "",
        notes: "",
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
    getBrands() {
      const path = "http://localhost:5000/brands";
      axios
        .get(path)
        .then((res) => {
          this.shoes = res.data.resource.brands;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // POST Function
    addShoe(payload) {
      const path = "http://localhost:5000/shoes";
      axios
        .post(path, payload)
        .then(() => {
          this.getShoes();
          this.message = "New Shoe Added!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getShoes();
        });
    },
    // DELETE Function
    deleteShoe(payload) {
      const path = `http://localhost:5000/shoes/${payload.id}`;
      axios
        .delete(path)
        .then(() => {
          this.getShoes();
          this.message = "Shoe Deleted!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getShoes();
        });
    },

    initForm() {
      this.addShoeForm.model = "";
      this.brand_id = "";
      this.model = "";
      this.nickname = "";
      this.distance = "";
      this.alertDistance = "";
      this.notes = "";
    },
    // For create modal to submit a new shoe
    onSubmit(event) {
      event.preventDefault();
      this.$refs.addShoeModal.hide();
      const payload = {
        brand_id: this.addShoeForm.brand_id,
        model: this.addShoeForm.model,
        nickname: this.addShoeForm.nickname,
        distance: this.addShoeForm.distance,
        alert_distance: this.addShoeForm.alertDistance,
        notes: this.notes,
      };
      this.addShoe(payload);
      this.initForm;
    },

    // For update modal to submit a new shoe
    onSubmitUpdate(event) {
      event.preventDefault();
      this.$refs.addShoeModal.hide();
      const payload = {
        brand_id: this.editShoeForm.brand_id,
        model: this.editShoeForm.model,
        nickname: this.editShoeForm.nickname,
        distance: this.editShoeForm.distance,
        alert_distance: this.editShoeForm.alertDistance,
        notes: this.notes,
      };
      this.updateShoe(payload, this.editForm.id);
      this.initForm;
    },

    onReset(event) {
      event.preventDefault();
      this.$refs.addShoeModal.hide();
      this.initForm();
    },
    /// PUT method
    updateShoe(payload, shoeID) {
      console.log(shoeID);
      const path = `http://localhost:5000/shoes/${shoeID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getShoes();
          this.message = "Shoe Updated!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getShoes();
        });
    },

    editShoe(shoe) {
      this.editShoeForm = shoe;
    },

    onResetUpdate(event) {
      event.preventDefault();
      this.$refs.editGameModal.hide();
      this.initForm();
      this.getShoes();
    },
  },
  created() {
    this.getBrands();
    this.getShoes();
    this.showMessage = false;
  },
};
</script>
