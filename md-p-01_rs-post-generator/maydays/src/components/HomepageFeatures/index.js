import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: '🚨 MayDay\'s Initiative 🚀',
    Svg: require('@site/static/img/maydays-1.svg').default,
    description: (
      <>
        Maydays is an ambitious initiative aiming to bring to life an innovative project every day throughout the month of May. 
      </>
    ),
  },
  {
    title: '🗓️ 1 Day - 1 Project 🏗️',
    Svg: require('@site/static/img/maydays-2.svg').default,
    description: (
      <>
        This daily showcase of skills highlights our creativity and ability to tackle diverse challenges.
      </>
    ),
  },
  {
    title: '🎯 A Creative Adventure 🖋️',
    Svg: require('@site/static/img/maydays-3.svg').default,
    description: (
      <>
        The goal of Maydays is to secure an apprenticeship contract for the fall by demonstrating our commitment and skills through these daily projects.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
