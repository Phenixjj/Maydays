import Image from "next/image";
import Background from "@/components/background";
import Button from "@/components/button";


export default function Home() {
  const discordUrl = "https://discord.gg/d7xC8fvdca";
  return (
    <main className="flex min-h-screen flex-col items-center justify-center">
      <Background className="absolute" />
      <div className="z-10">
        <h1 className="mt-10 font-orbitron text-9xl font-bold px-10">
          May Day's Initiative
        </h1>
        <p className="mt-9 font-oxygen font-bold text-6xl text-left px-10">
          Celebrating Innovation and <br /> <span className="mt-4 inline-block">Creativity</span>
        </p>
        <Button className="justify-self-start ml-10 mt-20" url={discordUrl} text="Join Today"/>
      </div>
    </main>
  );
}
