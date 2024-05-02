"use client";
import React, { useEffect, useState} from 'react';

import PropTypes from 'prop-types';

const TimeInput = ( {onTimeSelected} ) => {
    const [time, setTime] = useState(''); // State for the time input

    const handleTimeChange = (e) => {
        setTime(e.target.value);
    };

    useEffect(() => {
        console.log(time);
        onTimeSelected(time);
    }
    , [time, onTimeSelected]);

    return (
        <div>
            <label>
                Time:
                <input type="number" value={time} onChange={handleTimeChange}/>
                hours
            </label>
        </div>
    );
}

export default TimeInput;