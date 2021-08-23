import React from "react";
import { AnimatePresence } from "framer-motion";
import Meta from "./Meta";
import Navbar from "./Navbar";
export const Layout = () => {
  return (
    <>
      <Meta />
      <Navbar />
      <div id="wrapper">
        <AnimatePresence
          exitBeforeEnter
          initial={false} //disables animation when website is first loaded
        >
          {children}
        </AnimatePresence>
      </div>
      <Footer />
    </>
  );
};
