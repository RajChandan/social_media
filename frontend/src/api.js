import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const registerUser = async (formData) => {
    try {
        const response = await axios.post(`${API_URL}/user/register/`, formData,
            {
                headers: { "Content-Type": "multipart/form-data" }
            });
        return response.data;

    }
    catch (error) {
        console.log("Registration error : ", error);
        throw error.response.data;
    }
};


export const loginUser = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}/user/login/`, credentials, { headers: { "Content-Type": "application/json" } });
        return response.data;
    }
    catch (error) {
        console.log("Login error : ", error);
        throw error.response.data;
    }


};


export const githubLogin = async (code) => {
    try {
        const response = await axios.get(`${API_URL}/user/github/login/?code=${code}`);
        return response.data;
    }

    catch (error) {
        console.log("Github login error : ", error);
        throw error.response?.data || { error: "Github login failed" };
    }
};


export const getUserProfile = async (token) => {
    try {
        const response = await axios.get(`${API_URL}/user/profile/`, {
            headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
    }
    catch (error) {
        console.log("Profile fetch error : ", error);
        throw error.response.data;
    }
}