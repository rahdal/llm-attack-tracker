import React, { useState, useEffect } from 'react';
import { DataGrid, GridColDef } from '@mui/x-data-grid';

const columns: GridColDef[] = [
  { field: 'title', headerName: 'Title', width: 300 },
  { field: 'authors', headerName: 'Authors', width: 250 },
  { field: 'published_date', headerName: 'Published Date', width: 180 },
  { field: 'category', headerName: 'Category', width: 100 },
  {
    field: 'url',
    headerName: 'URL',
    width: 200,
    renderCell: (params) => (
      <a href={params.value} target="_blank" rel="noopener noreferrer">
        {params.value}
      </a>
    ),
  },
  {
    field: 'working',
    headerName: 'Working',
    width: 75,
    renderCell: (params) => (
      params.value ? <span style={{ fontSize: '1.2em' }}>✅</span> : <span style={{ fontSize: '1.2em' }}>❌</span>
    ),
  },
];

const DataTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/arxiv_papers?num_papers=100');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        // Adding the 'working' property to each row with a random value
        const rowsWithWorking = data.map(row => ({ ...row, working: Math.random() < 0.5 }));
        setRows(rowsWithWorking);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div style={{ height: '100%', width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        checkboxSelection={false}
      />
    </div>
  );
};

export default DataTable;
