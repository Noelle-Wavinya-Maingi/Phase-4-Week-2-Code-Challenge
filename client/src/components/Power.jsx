import { useEffect, useState } from "react";
// import { Link } from "react-router-dom";

function Power() {
  const [powers, setPowers] = useState([]);

  useEffect(() => {
    fetch("/api/powers")
      .then((res) => res.json())
      .then((responseData) => {
        console.log(responseData);
        setPowers(responseData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <section>
      <h2>All Powers</h2>
      <ul>
        {powers.map((power) => (
          <li key={power.id}>
            <h3>{power.name}</h3>
            <p>{power.description}</p>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Power;
