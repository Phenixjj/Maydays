"use client";
import React, { useState } from 'react';
import './main.css';
import CsvParserComponent from '@/components/CsvParserComponent';
import TimeInput from '@/components/TimeInput';
import Calculator from '@/components/Calculator';

export default function Home() {
  const [selectedEmployees, setSelectedEmployees] = useState([]);
  const [hours, setHours] = useState(0);

  return (
    <main className="main">
      <div className="mainDiv">
        <h1 className="bigTitle"><span className="welcomeTexjt">May Days J-1 </span>Meeting Cost Calculator </h1>
        <div className='info'>Import your CSV, and calculate the cost of your meeting ⏱️</div>
      </div>
      <div className='csvInputParser'>
      <CsvParserComponent onEmployeesSelected={setSelectedEmployees} />
      </div>
      <div className='timeInput'>
      <TimeInput onTimeSelected={setHours}/>
      </div>
      <div className='calculator'>
      <Calculator selectedEmployees={selectedEmployees} hours={hours}/>
    </div>
    </main>
  )
}