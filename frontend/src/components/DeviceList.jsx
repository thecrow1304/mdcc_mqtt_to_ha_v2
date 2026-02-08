
import React from "react";
import DeviceDetails from "./DeviceDetails";

const DeviceList = ({ devices }) => {
  return (
    <div>
      {Object.keys(devices).map((key) => (
        <DeviceDetails key={key} device={devices[key]} />
      ))}
    </div>
  );
};

export default DeviceList;
