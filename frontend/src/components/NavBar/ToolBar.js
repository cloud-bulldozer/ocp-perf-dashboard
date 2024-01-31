import { Toolbar, ToolbarGroup, ToolbarItem } from "@patternfly/react-core";
import React, { useEffect, useState } from "react";
import { Text4 } from "../PatternflyComponents/Text/Text";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

export const ToolBar = () => {
  const [active, setActive] = useState("/home");

  useEffect(() => {
    const path = window.location.href.split("/");
    let pathName = path[path.length - 1];
    if (pathName === "") pathName = "/home";
    setActive(pathName);
  }, []);

  const linkStyle = (value) => {
    const styles = {};
    if (active === value) {
      styles["color"] = "white";
      styles["borderBottom"] = "2px solid red";
    }
    return styles;
  };

  // Selectors for both ocpJobs and quayJobs
  const ocpJobResults = useSelector((state) => state.ocpJobs);
  const quayJobResults = useSelector((state) => state.quayJobs);
  const stubResults = useSelector((state) => state.stubData);

  const lastUpdated = (value) => {
    if (value === "/ocp") {
      return ocpJobResults.updatedTime
    } else if (value === "/quay") {
      return quayJobResults.updatedTime
    } else if (value === "/stub") {
      return stubResults.updatedTime
    } else {
      return ocpJobResults.updatedTime
    }
  }

  const NavItems = (
    <>
      <ToolbarItem>
        <Link
          to="/home"
          children={"Home"}
          style={linkStyle("/home")}
          onClick={() => setActive("/home")}
        />
      </ToolbarItem>
      <ToolbarItem>
        <Link
          to="/ocp"
          children={"OCP"}
          style={linkStyle("/ocp")}
          onClick={() => setActive("/ocp")}
        />
      </ToolbarItem>
      {/* New Quay ToolbarItem */}
      <ToolbarItem>
        <Link
          to="/quay"
          children={"Quay"}
          style={linkStyle("/quay")}
          onClick={() => setActive("/quay")}
        />
      </ToolbarItem>
      {/* Nav link for stub page */}
      <ToolbarItem>
        <Link
          to="/stub"
          children={"Stub"}
          style={linkStyle("/stub")}
          onClick={() => setActive("/stub")}
        />
      </ToolbarItem>
    </>
  );

  return (
    <>
      <Toolbar id="toolbar" isFullHeight={true} isStatic={true}>
        <ToolbarGroup>
          <ToolbarItem>
            <Text4 style={{ color: "#FFFFFF" }} value="CPT-Dashboard" />
          </ToolbarItem>
          {NavItems}
          <ToolbarItem align={{ default: "alignRight" }}>
            {/* Displaying the updated time for OCP or Quay based on the active path */}
            <Text4
              style={{ color: "#FFFFFF" }}
              value={`Last Updated Time | ${
                lastUpdated(active)
              }`}
            />
          </ToolbarItem>
        </ToolbarGroup>
      </Toolbar>
    </>
  );
};
