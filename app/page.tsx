// import Image from "next/image";
// import Link from "next/link";

// export default function Home() {
//   return (
//     <main className="flex flex-col items-center justify-center min-h-screen py-12 px-4 sm:px-6 lg:px-8 bg-gray-100">
//       <div className="max-w-5xl mx-auto">
//         {/* Header */}
//         <header className="mb-8">
//           <h1 className="text-4xl font-bold text-center text-gray-800">
//             Task Manager
//           </h1>
//           <p className="mt-2 text-lg text-center text-gray-600">
//             Manage your tasks efficiently
//           </p>
//         </header>

//         {/* Database Connectivity */}
//         <div className="w-full bg-gradient-to-b from-zinc-200 to-gray-200 border-b border-gray-300 rounded-xl p-4 mb-8 shadow-lg">
//           <p className="text-sm text-center text-gray-800">
//             Check the Database connectivity &nbsp;
//             <Link href="/api">
//               <a className="text-blue-600 hover:underline font-bold">Click here</a>
//             </Link>
//           </p>
//         </div>

//         {/* Task Form */}
//         <section className="bg-white shadow-lg rounded-xl p-6 mb-8">
//           <h2 className="text-xl font-semibold text-gray-800 mb-4">Create a New Task</h2>
//           {/* Task form inputs go here */}
//         </section>

//         {/* Task List */}
//         <section className="bg-white shadow-lg rounded-xl p-6">
//           <h2 className="text-xl font-semibold text-gray-800 mb-4">Task List</h2>
//           {/* Task list items go here */}
//         </section>
//       </div>
//     </main>
//   );
// }

import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30">
          Check the Database connectivity &nbsp;
          <Link href="/api">
            <code className="font-mono font-bold">Click here</code>
          </Link>
        </p>
       </div>
    </main>
  );
}

