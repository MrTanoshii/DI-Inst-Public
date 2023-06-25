import { Outlet } from "react-router-dom";

export const Home = () => {
  return (
    <h1>
      Home page
      <Outlet />
    </h1>
  );
};
