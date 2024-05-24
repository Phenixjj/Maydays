"use client";

import Image from "next/image";
import Background from "@/components/background";
import Button from "@/components/button";
import { useState, useEffect } from "react";
import betta1 from "../../public/static/img/betta_1.png";
import betta2 from "../../public/static/img/betta_2.png";
import betta3 from "../../public/static/img/betta_3.png";

export default function Home() {
  const discordUrl = "https://discord.gg/d7xC8fvdca";
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      setScrollY(window.scrollY);
    };
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);
  return (
    <main className="bg-[#0d0c0f] h-full flex min-h-screen flex-col relative">
      <Background className="" />
      <div
        className="absolute top-60 z-10"
        style={{ transform: `translateY(${scrollY * 0.2}px)` }}
      >
        <h1 className="mt-10 font-orbitron text-9xl font-bold px-32">
          May Day's Initiative
        </h1>
        <p className="mt-9 font-oxygen font-bold text-6xl text-left px-32">
          Celebrating Innovation and <br />
          <span className="mt-4 inline-block">Creativity</span>
        </p>
        <Button
          className="justify-self-start ml-32 mt-20"
          url={discordUrl}
          text="Join Today"
        />
      </div>
      <div
        className="mt-44 z-10"
        style={{ transform: `translateY(${scrollY * 0.1}px)` }}
      >
        <p className="font-oxygen font-bold text-4xl text-left px-32">
          Empowering Change Through Collaborative <br />
          <span className="mt-4 inline-block ">
            Projects and Inspiring Ideas
          </span>
        </p>
      </div>
      <div className="mt-20 flex flex-col">
        <div
          className=""
          style={{ transform: `translateY(${scrollY * 0.35}px)` }}
        >
          <h2 className="mt-20 font-montserrat text-5xl text-center text-[#EDEDED]">
            Join Us in Unleashing Innovation During May Day's
          </h2>
          <p className="mt-20 font-montserrat text-3xl text-center text-[#EDEDED] opacity-80">
            Explore a projects dedicated to fostering creativity and driving
            innovation. <br />
            <span className="mt-4 inline-block ">
              Discover how projects are shaping the future!
            </span>
          </p>
          <div className="flex justify-start mt-16 px-32">
            <ul className="mt-2">
              <li className="font-montserrat text-2xl">
                <h6 className="font-bold text-[#EDEDED]">
                  Inspire Collaborative Projects:
                </h6>
                <p className="mt-4 text-xl text-[#EDEDED] opacity-80">
                  May Day's aims to inspire individuals and teams to collaborate
                  on <br />
                  innovative projects that address real-world challenges. By
                  fostering
                  <br />
                  teamwork and creativity, we empower participants to make a
                  positive
                  <br />
                  impact.
                </p>
              </li>
              <li className="font-montserrat text-2xl">
                <h6 className="mt-8 font-bold text-[#EDEDED]">
                  Celebrate Creative Ideas:
                </h6>
                <p className="mt-4 text-xl text-[#EDEDED] opacity-80">
                  We celebrate and showcase diverse creative ideas that push
                  <br />
                  boundaries and spark new perspectives. From art and technology
                  to
                  <br />
                  social innovation, May Day's highlights the power of
                  imagination.
                </p>
              </li>
              <li className="font-montserrat text-2xl">
                <h6 className="mt-8 font-bold text-[#EDEDED]">
                  Encourage Networking and Learning:
                </h6>
                <p className="mt-4 text-xl text-[#EDEDED] opacity-80">
                  Our initiative provides a space for networking and learning,
                  <br />
                  connecting like-minded individuals and experts across various
                  fields.
                  <br />
                  Through workshops, discussions, and shared experiences, we aim
                  to
                  <br />
                  cultivate a supportive community of innovators.
                </p>
              </li>
            </ul>
          </div>
        </div>
        <div>
          <div className="flex justify-end pr-12">
            <Image
              alt="betta one fish swimming"
              src={betta1}
              placeholder="blur"
              quality={90}
              width={800}
            />
          </div>
        </div>
      </div>
      <div>
        <div
          className="flex justify-start pl-24"
          style={{ transform: `translateY(${scrollY * 0.1}px)` }}
        >
          <Image
            alt="betta one fish swimming"
            src={betta2}
            placeholder="blur"
            quality={90}
            width={550}
          />
        </div>
        <div className="flex mt-44 flex-row items-center">
          <p className="font-oxygen text-3xl text-left pl-44 text-[#EDEDED] opacity-80">
            Join us in this exciting journey of exploration and innovation
            <br />
            during May Day's! Together, let's create, inspire, and make a<br />
            difference.
            <br />
          </p>
          <Button
            className="justify-self-start ml-80 mt-20 mb-20"
            url={discordUrl}
            text="Join Today"
          />
        </div>
      </div>
      <div>
        <div>
          <div className="flex mt-22 justify-end">
            <Image
              alt="betta one fish swimming"
              src={betta3}
              placeholder="blur"
              quality={90}
              width={1250}
            />
          </div>
          <footer className="absolute mb-12 bottom-0 w-full text-center z-10 flex justify-between items-center px-4">
            <div className="ml-32">
              <a
                className="mr-8"
                href="https://discord.gg/d7xC8fvdca"
                target="_blank"
                rel="noopener noreferrer"
              >
                Discord
              </a>
              <a
                className="mr-8"
                href="https://www.linkedin.com/in/jean-lecigne-68aa0320a/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Contact
              </a>
            </div>
            <p className="mr-32">
              {new Date().getFullYear()} &copy; May Day’s !
            </p>
          </footer>
        </div>
      </div>
    </main>
  );
}
