
import React from "react";

const DeviceDetails = ({ device }) => {
  return (
    <div style={{ border: "1px solid #ccc", marginBottom: 10, padding: 10, borderRadius: 5 }}>
      <h2>{device.name} ({device.type})</h2>
      <p>Tenant: {device.tenant}</p>
      <ul>
        {device.entities.map((e) => (
          <li key={e}>{e}</li>
        ))}
      </ul>
    </div>
  );
};

export default DeviceDetails;
