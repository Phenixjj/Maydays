import React, { useEffect, useState } from "react";

const Calculator = ({ selectedEmployees, hours }) => {
  const [totalCost, setTotalCost] = useState(0);
  const hoursByYear = 1787;

  useEffect(() => {
    console.log("In calculator", selectedEmployees);
    setTotalCost(
      selectedEmployees.reduce((acc, employee) => {
        return acc + employee.salary / hoursByYear;
      }, 0) * hours
    );
  }, [selectedEmployees, hours]);

  useEffect(() => {
    console.log("total cost", totalCost);
    console.log("hours", hours);
    console.log("selected employees", selectedEmployees);
  }, [totalCost, hours, selectedEmployees]);

  return (
    <div>
      <h2>This meeting will cost : {totalCost} €</h2>
    </div>
  );
};

export default Calculator;
