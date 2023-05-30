<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12" md="10" lg="6">
        <v-row align="center" justify="center" dense>
          <v-card width="100%" style="padding: 5vh">
            <v-card-title
              ><h2><b>Live Tracing</b></h2></v-card-title
            >
            <v-card-text style="padding: 7vh">
              <v-form ref="stockForm" lazy-validation autocomplete="off">
                <v-col>
                  <v-row>
                    <v-col cols="12" sm="12" md="12"
                      ><v-text-field
                        v-model="search.stock"
                        :rules="[rules.notEmptyStock]"
                        label="Stock"
                        @input="formatText"
                        placeholder="Ex: IBM"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="search.min"
                        :rules="[rules.notEmptyValue]"
                        prefix="R$"
                        label="Buy Value"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="search.max"
                        :rules="[rules.notEmptyValue]"
                        prefix="R$"
                        label="Sell Value"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-btn
                      color="#5BD098"
                      block
                      dark
                      :disabled="!isFormValid"
                      @click="createSearch"
                      >Submit</v-btn
                    >
                    <span>{{ errorMessage }}</span>
                  </v-row>
                </v-col>
              </v-form>
              <v-row
                align="center"
                justify="center"
                class="mt-4"
                v-if="hasStock"
              >
                <v-col>
                  <v-row class="mt-2">
                    <h1>Stock: {{ current.stock }}</h1>
                  </v-row>
                  <v-row class="mt-2">
                    <h2 class="mt-2">Current value: R$102,00</h2>
                  </v-row>
                  <v-row class="mt-2">
                    <h2 class="mt-2">Action: BUY</h2>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-row>
        <v-row> </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      errorMessage: "",
      hasStock: false,
      isFormValid: false,
      search: {
        stock: "",
        min: null,
        max: null,
      },
      current: {
        stock: "",
        min: null,
        max: null,
      },
      rules: {
        notEmptyValue: (value) => {
          if (value >= 0 && value != null) return true;
          return "You must enter a value.";
        },
        notEmptyStock: (v) => !!v || "Stock is required",
      },
    };
  },
  watch: {
    "search.stock": function () {
      this.validateForm();
    },
    "search.min": function () {
      this.validateForm();
    },
    "search.max": function () {
      this.validateForm();
    },
  },
  methods: {
    formatText() {
      this.search.stock = this.search.stock.toUpperCase();
    },
    createSearch() {
      if (this.$refs.stockForm.validate()) {
        this.setCurrent(this.search);
        this.resetForm();
        this.hasStock = true;
      } else {
        this.errorMessage = "Campos do formulário estão vazios";
      }
    },
    setCurrent(stock) {
      this.current.stock = stock.stock;
    },
    resetForm() {
      this.search.stock = "";
      this.search.min = null;
      this.search.max = null;
    },
    validateForm() {
      if (this.search.stock && (this.search.min >= 0 && this.search.min != null) && (this.search.max >= 0 && this.search.max != null)) {
        this.isFormValid = true;
      } else {
        this.isFormValid = false;
      }
    },
  },
};
</script>
