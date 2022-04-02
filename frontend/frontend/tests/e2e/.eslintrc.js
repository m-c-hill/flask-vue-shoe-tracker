module.exports = {
  plugins: ["cypress"],
  env: {
    mocha: true,
    "cypress/globals": true,
  },
  rules: {
    "vue/multi-word-component-names": "off",
    strict: "off",
  },
};
