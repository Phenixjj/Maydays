import Image from 'next/image'
// import backgroundHero from '../../public/static/img/Default_2_Betta_Siamese_Fishing_Fish_swimming_together_and_tur_0_return.jpg'
import backgroundHero from '../../public/background_x2_fade.jpg'
 
export default function Background({className}) {
  return (
    <Image
      alt="betta fish swimming together"
      src={backgroundHero}
      placeholder="blur"
      quality={100}
      fill={false}
      className={className}
      unoptimized
    />
  )
}