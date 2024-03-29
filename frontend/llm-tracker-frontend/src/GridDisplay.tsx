import React, { useState, useEffect } from 'react';
import { DataGrid, GridColDef } from '@mui/x-data-grid';

const columns: GridColDef[] = [
  { field: 'title', headerName: 'Title', width: 350 },
  { field: 'authors', headerName: 'Authors', width: 250 },
  { field: 'published_date', headerName: 'Published Date', width: 180 },
  {
    field: 'url',
    headerName: 'URL',
    width: 250,
    renderCell: (params) => (
      <a href={params.value} target="_blank" rel="noopener noreferrer">
        {params.value}
      </a>
    ),
  },
];

const DataTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/arxiv_papers?num_papers=10');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setRows(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize="5"
        checkboxSelection
      />
    </div>
  );
};

export default DataTable;
