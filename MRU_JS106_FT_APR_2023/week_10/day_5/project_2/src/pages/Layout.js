import { Outlet } from "react-router-dom";

export const Layout = () => {
  return (
    <>
      <h1>Basic Layout</h1>
      <Outlet />
    </>
  );
};
