const express = require('express');
const cors = require('cors');
const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

app.post('/insta', (req, res) => {
  const instaUrl = req.body.url;
  console.log('Received Instagram URL:', instaUrl);
  res.status(200).send('URL received');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
