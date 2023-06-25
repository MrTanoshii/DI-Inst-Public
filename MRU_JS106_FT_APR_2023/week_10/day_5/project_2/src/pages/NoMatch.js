import { Outlet } from "react-router-dom";

export const NoMatch = () => {
  return (
    <h1>
      404 Page not found
      <Outlet />
    </h1>
  );
};
