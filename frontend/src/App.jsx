
import React, { useEffect, useState } from "react";
import DeviceList from "./components/DeviceList";
import { getDevices } from "./api";

function App() {
  const [devices, setDevices] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const data = await getDevices();
      setDevices(data);
    };
    fetchData();
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>MQTT Dynamic Entities Dashboard</h1>
      <DeviceList devices={devices} />
    </div>
  );
}

export default App;
