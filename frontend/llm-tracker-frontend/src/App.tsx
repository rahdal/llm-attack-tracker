import React from 'react';
import { Container, Typography } from '@mui/material';
import DataTable from './GridDisplay'; // Assuming DataTable is correctly implemented

function App() {
  return (
    <Container>
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
        <img src="/UM_GPT.svg" alt="Image" style={{ marginRight: '10px', width: '50px', height: '50px', verticalAlign: 'middle' }} />
        <Typography variant="h4" component="h1" style={{ lineHeight: '50px', marginBottom: 0 }}>
          LLM Exploits
        </Typography>
      </div>
      <DataTable />
    </Container>
  );
}

export default App;
