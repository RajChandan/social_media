import {useState} from "react";
import { registerUser } from "../api";
import {useNavigate} from "react-router-dom";

const Register = () =>
{
    const [formData,setFormData] = useState({username:"",email:"",password:""});
    const [error,setError] = useState(null);
    //const navigate =   useNavigate();

    const handleChange = (e) =>
    {
        setFormData({...formData,[e.target.name]:[e.target.value]});
    };

    const handleSubmit = async(e) =>
    {
        e.preventDefault();
        try
        {
            await registerUser(formData);
            //navigate("/login");
        }
        catch(err)
        {
            setError(err.message || "Registration failed");
        }
    };
    

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md w-96">
                <h2 className="text-2xl font-bold text-center mb-4">Register</h2>
                {error && <p className="text-red-500">{error}</p>}
                <input type="text" name="username" placeholder="username" className="w-full p-2 mb-2 border rounded" onChange={handleChange} required/>
                <input type="email" name="email" placeholder="Email" className="w-full p-2 mb-2 border rounded" onChange={handleChange} required/>
                <input type="password" name="password" placeholder="Password" className="w-full p-2 mb-2 border rounded" onChange={handleChange} required/>
                <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">Register</button>
            </form>
            
        </div>
    );
};

export default Register;