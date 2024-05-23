"use client"
import React from "react"
import cn from "classnames"

export default function Button({className, url, text}) {
    const handleClick = () => {
        window.open(url, '_blank');
      };
    return (
        <button className={cn("outline transition hover:bg-white text-white hover:text-black font-bold py-3 px-10 rounded-full", className)} onClick={handleClick}>
            {text}
        </button>
    )
}