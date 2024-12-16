import axios from "axios";

const API_BASE_URL = "http://localhost:3000";
const API_KEY = "hFBSVPOkGH8oIBEMEwvRHxxXfNdQjrs7sBesTEoPVxk=_48bc0a559d4c568bfa32f96f2e806c8f";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
  },
});

export const loginUser = async (email, password) => {
  const response = await api.post("/user/login", { email, password });
  return response.data;
};

export const uploadFileForPrediction = async (token, file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(`${API_BASE_URL}/imagenet/imagenet-label`, formData, {
    headers: {
      Authorization: `Bearer ${token}`,
      "x-api-key": API_KEY,
    },
  });
  return response.data;
};
