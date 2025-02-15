import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register from "./pages/register";
import Login from "./pages/login";
import Profile from "./pages/profile";
import ProtectedRoute from "./components/protectedroute";

function App() {
  return (<Router>
    <Routes>
      <Route path="/register" element={<Register />}></Route>
      <Route path="/login" element={<Login />}></Route>
      <Route path="/profile" element={<ProtectedRoute><Profile />
      </ProtectedRoute>}>
      </Route>
    </Routes>
  </Router>);
}

export default App;