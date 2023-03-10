import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AppContext } from "../../contexts/AppProvider";

const Logo = ({ className }) => {
  const { homeData } = useContext(AppContext);
  console.log(homeData.image);

  if (homeData.image) {
    return (
      <Link id="Logo" to={"/"} className={` ${className || ""}`}>
        <figure className={" max-w-[6rem] "}>
          <img
            className={" w-full h-full"}
            src={`http://localhost:8000${homeData.image}`}
            alt="Logo"
          />
        </figure>
      </Link>
    );
  } else {
    return (
      <Link id="Logo" to={"/"} className={`${className || ""}`}>
        <div className="p-6 py-2 SmallPhones:p-4 SmallPhones:py-1 border rounded border-gray-600">
          <p className={"text-base"}>LOGO</p>
        </div>
      </Link>
    );
  }
};

export default Logo;
