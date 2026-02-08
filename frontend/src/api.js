
export const getDevices = async () => {
  const res = await fetch("/api/devices");
  return res.json();
};
