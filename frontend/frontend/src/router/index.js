import Vue from "vue";
import VueRouter from "vue-router";
import SharkComp from "../components/SharkComp.vue";
import ShoeTracker from "../components/ShoeTracker.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: SharkComp,
  },
  {
    path: "/shoes",
    name: "Shoes",
    component: ShoeTracker,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
