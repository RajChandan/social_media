import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const registerUser = async (formData) => {
    try
    {
        const response = await axios.post(`${API_URL}/user/register/`,formData,
        {
            headers : {"Content-Type":"multipart/form-data"}
        });
        return response.data;

    }
    catch (error)
    {
        console.log("Registration error : ",error);
        throw error.response.data;
    }
};