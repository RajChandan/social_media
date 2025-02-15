import { useEffect, useState } from "react";
import { getUserProfile } from "../api";
import { useNavigate } from "react-router-dom";

const Profile = () => {
    const [user, setUser] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();


    //fetch user profile when component mount//

    useEffect(() => {
        const fetchProfile = async () => {
            const token = localStorage.getItem("token");
            if (!token) {
                navigate("/login");
                return;
            }

            try {
                const data = getUserProfile(token);
                setUser(data);
            }
            catch (error) {
                setError("Failed to fetch profile, please login again");
                localStorage.removeItem("token");
                navigate("/login");
            }

        };
        fetchProfile();
    }, [navigate]);


    const handleLogout = () => {
        localStorage.removeItem("token");
        navigate("/login");
    };

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-100">
                <p className="text-red-500">{error}</p>
            </div>
        );
    }

    if (!user) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-100">
                <p>Loading ...</p>
            </div>
        );
    }

    return (<div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="bg-white p-6 rounded-lg shadow-md w-96">
            <h2 className="text-2xl font-bold text-center mb-4">Profile</h2>
            <img src={user.profile_picture || "https://via.placeholder.com/150"}
                alt="profile picture"
                className="w-32 h-32 rounded-full mx-auto mb-4" />
        </div>

    </div>);

}

export default Profile;
