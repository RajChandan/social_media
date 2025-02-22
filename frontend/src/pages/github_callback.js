import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { githubLogin } from "../api";

const GitHubCallback = () => {
    const navigate = useNavigate();
    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const accessToken = urlParams.get("access_token");
        const refreshToken = urlParams.get("refresh_token");
        if (accessToken && refreshToken) {
            localStorage.setItem("token", accessToken);
            navigate("/profile");
        }
        else {
            navigate("/login");
        }
    }, [navigate]);
    return <div>Processing github login</div>;
}

export default GitHubCallback;