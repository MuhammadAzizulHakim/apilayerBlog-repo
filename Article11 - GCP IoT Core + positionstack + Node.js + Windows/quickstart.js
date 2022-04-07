const iot = require('@google-cloud/iot');
const client = new iot.v1.DeviceManagerClient();

async function quickstart() {
  const projectId = await client.getProjectId();
  const parent = client.locationPath(projectId, 'us-central1');
  const [resources] = await client.listDeviceRegistries({parent});
  console.log(`${resources.length} resource(s) found.`);
  for (const resource of resources) {
    console.log(resource);
  }
}
quickstart();
