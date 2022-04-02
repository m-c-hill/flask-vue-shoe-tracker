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
      <div class="row">
        <div class="col-sm-12"></div>
        <!-- Alert message -->
        <button type="button" class="btn btn-success">Add Shoe</button>
        <br />
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
            <tr>
              <!-- Dummy data to be removed -->
              <td>Saucony</td>
              <td>Endorphin Speed 2</td>
              <td>Jan '22</td>
              <td>304</td>
              <td>Reserved for track and tempo sessions.</td>
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
