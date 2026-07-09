import { Suspense } from "react";
import { IdeaView } from "./IdeaView";

export default async function PaginaIdea({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return (
    <Suspense>
      <IdeaView projectId={id} />
    </Suspense>
  );
}
