import './GridDisplay'
import DataTable from './GridDisplay'
import { Container,Typography } from '@mui/material'

function App() {

  return (
    <Container>
      <Typography variant="h4" component="h1" sx={{ mb: 2 }}>
        LLM Exploits
      </Typography>
      <DataTable></DataTable>
    </Container>
  )
}

export default App
