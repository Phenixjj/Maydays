"use client";
import React, { useState, useCallback, useEffect } from "react";
import csv from "csv-parser";
import { useDropzone } from "react-dropzone";

const CsvParserComponent = ({ onEmployeesSelected }) => {
  const [employees, setEmployees] = useState([]);
  const [selectedEmployees, setSelectedEmployees] = useState([]);

  const selectEmployee = (e, id) => {
    setEmployees((prevEmployees) =>
      prevEmployees.map((employee) => {
        if (employee.id === id) {
          const updatedEmployee = { ...employee, selected: !employee.selected };
          return updatedEmployee;
        } else {
          return employee;
        }
      })
    );
    setSelectedEmployees((prevSelectedEmployees) => {
        if (prevSelectedEmployees.find((employee) => employee.id === id)) {
            return prevSelectedEmployees.filter((employee) => employee.id !== id);
        } else {
            return [...prevSelectedEmployees, employees.find((employee) => employee.id === id)];
        }
    });
  };

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();

      reader.onload = (e) => {
        const text = e.target.result;
        const results = [];

        text
          .trim()
          .split("\n")
          .forEach((line, index) => {
            const data = line.split(",");
            const employee = {
              id: index,
              name: data[0], // Assuming the first column is the name
              salary: parseInt(data[1].replace('\r', '')), // Assuming the second column is the salary
              selected: false,
            };
            results.push(employee);
          });
        setEmployees(results.slice(1));
      };

      reader.readAsText(file);
    });
  }, []);

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  useEffect(() => {
    console.log("coucou from selected employees",selectedEmployees);
    onEmployeesSelected(selectedEmployees);
  }, [selectedEmployees, onEmployeesSelected]);

  return (
    <div>
      <div {...getRootProps()}>
        <input {...getInputProps()} />
        <p>Drag 'n' drop files here, or click to select files</p>
      </div>
      <div>
        {employees.map((employee, index) => (
          <div key={index}>
            <input
              type="checkbox"
              checked={employee.selected}
              onChange={(e) => selectEmployee(e, employee.id)}
            />
            <span>{employee.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CsvParserComponent;
