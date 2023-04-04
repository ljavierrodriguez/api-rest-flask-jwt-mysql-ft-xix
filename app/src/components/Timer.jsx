import React, { useEffect, useState } from 'react'

const Timer = ({ className, duration }) => {
    //console.log(duration)
    const [hours, setHours] = useState(0);
    const [minutes, setMinutes] = useState(0);
    const [seconds, setSeconds] = useState(0);
    const [counter, setCounter] = useState(duration);

    useEffect(() => {
        const id = setInterval(() => {
            
            setCounter(counter => {
                if(counter > 0){
                    setTime(counter);
                    return counter - 1
                }
            });
        }, 1000)

        return () => {
            clearInterval(id);
        }
    }, [])

    useEffect(() => {
        setCounter(duration);
    }, [duration])

    const setTime = (counter) => {
        setHours(Math.floor(counter / 3600))
        setMinutes(Math.floor(counter / 60) % 60)
        setSeconds(counter % 60)
    }

    return (
        <div className={className}>
            {hours < 10 ? `0${hours}`: hours }:{minutes < 10 ? `0${minutes}`: minutes }:{seconds < 10 ? `0${seconds}`: seconds }
        </div>
    )
}

export default Timer